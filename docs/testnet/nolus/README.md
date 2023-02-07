# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.1.39 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)




## Chain explorer
[https://explorer.kjnodes.com/nolus-testnet](https://explorer.kjnodes.com/nolus-testnet)

## Public endpoints

* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)
* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* grpc: [https://nolus-testnet.grpc.kjnodes.com](https://nolus-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (40)
```bash
peers="7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,e4b7228ccadf3180e6e323aa4c0c97946ac054dc@65.109.112.20:11134,038eef443b6bab9c28f9109599cd8733b3eb8dff@65.21.185.92:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,8ca0bffdf45aa4aaa4624c6d4c3e258a8c595591@65.108.43.58:27659,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,1278e67b0f6523c20e665109dd092ef20d6fd70e@45.67.230.23:26656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,1cb8223111a5fb8a631d73aa3bcd7abd2ef41ba7@45.87.104.84:1184,85c5ef9ff695574abdf1ab38fb1196bc6482aec5@89.252.21.37:26656,d6f7b2380e994c6b8f6fcb05b4a326ae2d1f202a@37.123.114.30:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,77f535f833732fa794f7c4837060ae7ecd98f3a4@89.163.142.196:43656,f09a8ba06a00d1edc517995040313732f94c2b56@95.214.55.155:18656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,b18f05bafd90cde6391d41880fc2d2461034a5de@20.189.72.168:26656,61ad400ccad76d73e2e2102ba9f3cf527c879864@65.108.231.87:26656,fac035258738be9be98957d5d012d24841d2e5eb@85.10.197.4:16656,6435149033788abd03e6ff39cb4485095a6878e4@95.214.55.62:47656,d8d4765d15f7cdd878af8cd6263fa11c05b013c7@146.190.121.227:26656,6b1de499ecaf6c7e305c8a7ba928123f232cec9b@194.163.185.154:26656,c5d5ad5061871c29b3dc08d525992f45cbc901d9@194.104.136.99:37656,903a6f84c099ae0127b4d5cfcf016e91164679e1@5.78.70.114:26656,7a942f2030c3e1a28ba82dbe3b0331275de597c8@92.53.65.56:26656,7c2ea36064077da73d0ad5b60d8ef215acbee50b@161.97.79.100:36656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,fa0a2fe57c2ab28aee6cc0be4eddbc68d6587a75@95.217.165.189:26656,574a94ae197e11183b292e05161baa2558f79ea1@194.163.176.105:32656,9f8e23a45a79ebd46abd47b916a51a47729c4df0@142.132.248.168:26656,93b90db2cb18bfa490c7dc4dddd0720ec9cfcfb5@212.24.101.2:26656,f19cc53d62df3713f7e1a651fe6022010954fbf6@93.84.135.230:49656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
