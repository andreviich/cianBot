document.getElementById("startBrowser").addEventListener("click", ()=>{eel.runChrome()}, false);
document.getElementById("startParsing").addEventListener("click", ()=>{eel.startParsing(); console.log('Работаю')}, false);
// document.getElementById("button-date").addEventListener("click", ()=>{eel.get_date()}, false);
// document.getElementById("button-ip").addEventListener("click", ()=>{eel.get_ip()}, false);

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}