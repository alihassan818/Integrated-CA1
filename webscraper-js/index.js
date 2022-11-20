const puppeteer = require('puppeteer');
const csv = require('csv-writer').createObjectCsvWriter;

const write = csv({
    path: 'F:\\fiverr\\ws\\webscraper-js\\data.csv',
    header: [
        {id: 'name', title: 'article-name'},
        {id: 'link', title: 'article-link'},
        {id: 'war', title: 'About War?'}
    ]
});

fileContent = [];

async function scrapeArticle(url) {
    const browser = await puppeteer.launch({
        headless: true
        
    });
    const page = await browser.newPage();
    await page.goto(url);

    const lnks = await page.$$('.ssrcss-1ynlzyd-PromoLink');
    for (let i = 0; i < lnks.length; i++) {
        lnk = await (await lnks[i].getProperty('href')).jsonValue();
        //link of article
        title = await (await lnks[i].getProperty('innerText')).jsonValue();
        //title of article

        if (title.includes("war")) {
            abt_war = "Yes"
        } else if(title.includes("War")) {
            abt_war = "Yes"
        } else {
            abt_war = "No"
        }

        await fileContent.push({name: title, link: lnk, war: abt_war})
    }
    await write.writeRecords(fileContent)
    .then( () => {
        console.log("done")
        browser.close()
    })
    
}

scrapeArticle('https://www.bbc.co.uk/search?q=ukraine&d=news_ps');