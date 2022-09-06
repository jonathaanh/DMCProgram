const PDFDocument = require('pdfkit');
var fs = require('fs');

let doc = new PDFDocument({size: 'LETTER', bufferPages: true});

doc.pipe(fs.createWriteStream('pdfs/test.pdf'));
doc.fontSize(12);
doc.image('logo.jpeg',doc.page.width/2 - 190/2,doc.y,{
	width:190, height:190, link:"www.drydockweb.com"
	});
doc.addPage()
doc.addPage()
var array = fs.readFileSync("sample.txt").toString().split("\n");

let bottom = doc.page.margins.bottom;
doc.page.margins.bottom = 0;
doc.text('Page 1', 0.5 * (doc.page.width - 100), doc.page.height - 50,
{
	width: 100,
	align: 'center',
	lineBreak: false,
})

// Reset text writer position
doc.text('', 50, 50)
doc.page.margins.bottom = bottom;
let pageNumber = 1;

doc.on('pageAdded', () => {
	pageNumber++
	let bottom = doc.page.margins.bottom;
	doc.page.margins.bottom = 0;

	doc.text(
		'Page ' + pageNumber, 
		0.5 * (doc.page.width - 100),
		doc.page.height - 50,
		{
			width: 100,
			align: 'center',
			lineBreak: false,
		})

	// Reset text writer position
	doc.text('', 50, 50);
	doc.page.margins.bottom = bottom;
})
var calculations = [];
for(i in array) {
	var char = array[i].substring(0,3);
	var last = array[i].substring(3);
	if(char == "<T>"){
		console.log(last);
		doc.font("Helvetica-Bold").text(last,{ destination: last });
		calculations.push(last);
		calculations.push(pageNumber);
		//doc.font("Helvetica-Bold").text(last);
	}else if(char == "<E>"){
		console.log(last);
		doc.text(last);
	}else if(char == "<I>"){
		//console.log(last);
		doc.image(last, doc.page.width/2 - 190/2,doc.y,{
			width:190, height:190
			});
	}else if(char == "<R>"){
		console.log(last);
		doc.text(last);
	}else if(char == "<B>"){
		console.log(last);
		doc.text(last);
	}else{
		console.log(array[i]);
		doc.font("Helvetica").text(array[i]);
	}
}	
doc.switchToPage(1);
doc.fontSize(20).text('Table of Contents');
doc.text(" ");
doc.fontSize(12);
for(let i = 0; i < calculations.length; i = i + 2){
	
	doc.font("Helvetica-Bold").text(calculations[i]+" . . . . . . . . . . . . . . . . . . . . . . . . . . . "+calculations[i+1], {
		goTo: calculations[i]});
	doc.text(" ");
}
doc.end();