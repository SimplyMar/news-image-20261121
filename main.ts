import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const MAX_BYTES = 1_048_576;
const MAX_DIM = 1024;

function validatePng(buf: Buffer, label: string): { size: number; width: number; height: number } {
  const size = buf.length;
  if (size <= 0 || size > MAX_BYTES) {
    throw new Error(`${label}: invalid size ${size} bytes (expected 1..${MAX_BYTES})`);
  }
  if (size < 24 || !buf.subarray(0, 8).equals(PNG_MAGIC)) {
    throw new Error(`${label}: invalid PNG magic bytes`);
  }
  if (buf.subarray(12, 16).toString("ascii") !== "IHDR") {
    throw new Error(`${label}: missing IHDR chunk`);
  }
  const width = buf.readUInt32BE(16);
  const height = buf.readUInt32BE(20);
  if (width < 1 || width > MAX_DIM || height < 1 || height > MAX_DIM) {
    throw new Error(`${label}: invalid dimensions ${width}x${height} (expected 1..${MAX_DIM})`);
  }
  return { size, width, height };
}

const entryPath = join(fileURLToPath(new URL(".", import.meta.url)), "entry.png");
const sourceBuf = readFileSync(entryPath);
const { size, width, height } = validatePng(sourceBuf, entryPath);

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outputDir, { recursive: true });

const destPath = join(outputDir, "entry.png");
writeFileSync(destPath, sourceBuf);

const writtenBuf = readFileSync(destPath);
const verified = validatePng(writtenBuf, destPath);
if (verified.size !== size || !writtenBuf.equals(sourceBuf)) {
  throw new Error(`Verification mismatch between ${entryPath} and ${destPath}`);
}

process.stdout.write(`copied entry.png (${size} bytes, ${width}x${height}) to ${outputDir}\n`);
