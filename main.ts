// A working news-image-daily entry (Node 22, standard library only): its image is the entry.png beside this file, and
// the program copies it to /output/entry.png. A starting point, not a winner: replace the image. The gate takes a
// whole PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels, and the judge sees exactly the bytes copied.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, statSync } from 'node:fs';
import { join } from 'node:path';

const entryPath = new URL('./entry.png', import.meta.url);
if (!existsSync(entryPath)) {
  throw new Error(`entry.png not found next to main.ts: ${entryPath}`);
}

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outputDir, { recursive: true });

const destPath = join(outputDir, 'entry.png');
copyFileSync(entryPath, destPath);

const { size } = statSync(destPath);
console.log(`copied entry.png (${size} bytes) to ${outputDir}`);
