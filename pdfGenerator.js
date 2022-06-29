const PDFDocument = require('pdfkit');
const fs = require('fs');

let pdfDoc = new PDFDocument({size: [215.9,279.4], margins : { 
	top: 25.4,
	bottom:25.4,
	left: 25.4,
	right: 25.4
}});
pdfDoc.pipe(fs.createWriteStream('pdfs/test.pdf'));
pdfDoc.text("My Sample PDF Document");
pdfDoc.addPage();

pdfDoc.end();