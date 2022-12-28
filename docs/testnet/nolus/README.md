# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.1.39 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)


## Public endpoints

* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (35)
```
peers="3cadae7324e9bf129b76bc489cd080535d03f3d2@176.9.22.117:55656,a7a48a15db2140201f22047ee9abbc0b259c1f92@194.163.129.102:26656,89aaf76a23b16bd57a1982e7b304fd998a49942a@65.109.85.226:9000,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,8ca0bffdf45aa4aaa4624c6d4c3e258a8c595591@65.108.43.58:27659,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,ef404b6e855c70ee51532ca83407350d2379bdec@5.161.101.185:26656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,d694df8e90ddf6102be5c825e57fc58d55217629@143.198.205.193:26656,ac86c1678e20a87bf2f036741932910869726337@135.181.222.185:15656,43b2582d9f63b46df12879729e8d3d1daa899ef4@144.126.154.230:26656,301dcb25951a0ebd6a36e09e612c85dc3aea3767@95.70.160.37:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,f6422b4cbe9095529432231e3ed397626378a938@162.55.1.2:44656,d788696b4ea9ddd295f86f0cb10a6be86a94764c@161.97.136.72:26656,ac38d6ef4cc254c689bcd6bcaf2a359672e4405b@77.238.148.219:26656,1cb8223111a5fb8a631d73aa3bcd7abd2ef41ba7@45.87.104.84:1184,6d5921160c688c2e4e3b510fcfa48496e74cf2c6@80.92.204.247:37656,c8c6249b27b4a34aac554d12b0107cc6421098ef@65.108.126.35:24656,0990266d3b28a8941e98f9035b5410b627f79003@110.4.162.53:26656,9a1d174e1983d56fb40f674fe0e19384ece6320d@194.60.201.171:26656,b6c8dc38a5dba19a3f10d23b3572065db9265fa3@65.109.85.225:9000,dc11cb38586c91b1149d626a59454674c3e969f4@217.76.62.87:26656,71cb32264e19b25fc313d0ff8baf24fe948576a1@65.109.30.12:60656,1444e8387381acb0d432c1aa9b78db3749e9568a@38.242.202.200:26656,ce81aede998514371277a57979712392ffc3d46c@45.142.214.3:37656,55acbb36f6e18ce9d5034c1e0f615bf13ee1ae27@195.2.80.63:43656,18ead126cc62f5aee200a8322b5c97fca6d05880@173.212.194.45:26656,60c57c5b7215c84260249768cf66ae550142af9f@141.98.169.25:26656,fa0a2fe57c2ab28aee6cc0be4eddbc68d6587a75@95.217.165.189:26656,9fa1e4ded1a41a4498781f93a209053a7c3f36e8@170.187.231.63:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nolus/config/config.toml
```
