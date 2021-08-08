const Discord = require('discord.js');
const client = new Discord.Client();
const request = require('request');
client.on('ready', () => {
	console.log(`Bot started!\nUsername: ${client.user.username}\nId: ${client.user.id}`);
});
client.on("message", (message) => {
  var content = message.content.split(" ");
  if (content[0] == '.stats') {
     request('https://mcapi.us/server/status?ip=14b14t.com', function (body) {
      let apiJSON = body;
      let result = JSON.parse(apiJSON);
      const playersresult = (result.players.now);
      const motdresult = (result.motd);
      let embed = new Discord.MessageEmbed()
      embed.setColor('#0099ff')
      embed.setTitle("");
      embed.setFooter(`14b14t.com`, 'https://cdn.discordapp.com/icons/868751094174601227/ffd3b0ad26532ed97c9728155e2bfa17.png');
      embed.setDescription(`Server Stats\n\nOnline players: ${playersresult}\nMotd: ${motdresult}`)
      message.channel.send(embed); }
    )};
});
client.login('');
