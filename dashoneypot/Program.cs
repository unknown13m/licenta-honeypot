using MongoDB.Driver;
using MongoDB.Bson;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddRazorPages();

var client = new MongoClient("mongodb://81.181.166.65:27017");
var database = client.GetDatabase("honeypot_db");
var collection = database.GetCollection<BsonDocument>("attacks");

builder.Services.AddSingleton(collection);

var app = builder.Build();
app.UseStaticFiles();
app.UseRouting();
app.MapRazorPages();
app.Run();