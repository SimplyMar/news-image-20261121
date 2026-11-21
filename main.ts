import { copyFileSync, existsSync, mkdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const MAX_BYTES = 1_048_576;
const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const here = fileURLToPath(new URL('.', import.meta.url));
const entryPath = join(here, 'entry.png');

if (!existsSync(entryPath)) {
  throw new Error(`entry.png not found next to main.ts: ${entryPath}`);
}

function verifyPng(file: string): number {
  const size = statSync(file).size;
  if (size <= 0 || size > MAX_BYTES) {
    throw new Error(`entry.png out of size limit: ${size} bytes`);
  }
  const buf = readFileSync(file);
  if (!buf.subarray(0, 8).equals(PNG_MAGIC)) {
    throw new Error('entry.png missing PNG signature');
  }
  const width = buf.readUInt32BE(16);
  const height = buf.readUInt32BE(20);
  if (width > 1024 || height > 1024 || width === 0 || height === 0) {
    throw new Error(`entry.png dimensions out of bounds: ${width}x${height}`);
  }
  return size;
}

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outputDir, { recursive: true });
const destPath = join(outputDir, 'entry.png');
copyFileSync(entryPath, destPath);
const bytes = verifyPng(destPath);
process.stdout.write(`copied entry.png (${bytes} bytes) to ${outputDir}\n`);
