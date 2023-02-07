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

**live-peers** (35)
```bash
peers="5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,143c212edac4e29e00218214205f1011d7376b02@135.181.38.11:26656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,55acbb36f6e18ce9d5034c1e0f615bf13ee1ae27@195.2.80.63:43656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,1278e67b0f6523c20e665109dd092ef20d6fd70e@45.67.230.23:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,b18f05bafd90cde6391d41880fc2d2461034a5de@20.189.72.168:26656,681ecb99467dd00a586d9499a1002f2829f1a02d@65.109.85.208:29656,7a942f2030c3e1a28ba82dbe3b0331275de597c8@92.53.65.56:26656,9d761ce1e1dc54ded3ab82ce0256c27631b5e82c@173.212.241.80:43656,3b50653b3b9ccca9fb4e88617f6f30bd1a1a5224@188.120.247.25:43656,6435149033788abd03e6ff39cb4485095a6878e4@95.214.55.62:47656,e4b7228ccadf3180e6e323aa4c0c97946ac054dc@65.109.112.20:11134,98907b8c92c003aa2d003bb5d47e5ae6e34b0732@77.51.200.79:46656,43294ababb32039af22c5bac16451d7a2b056f33@77.94.99.52:26656,7c2ea36064077da73d0ad5b60d8ef215acbee50b@161.97.79.100:36656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,8ca0bffdf45aa4aaa4624c6d4c3e258a8c595591@65.108.43.58:27659,a9cce28334e6111c74934140ef915abb20968d2f@89.252.21.37:26656,1cb8223111a5fb8a631d73aa3bcd7abd2ef41ba7@45.87.104.84:1184,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,2f733fee182504c70f38be10f083263ead4a579e@14.238.7.58:26656,56c262dbc7ccc509f1768768d87f8a53bf037f02@65.21.92.150:26656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,7f6bd81ef074767a0d9c36177c9288dd79915619@194.163.136.160:26656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,1e5990b6b0df623e05a53d845982040e68698940@188.43.118.19:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
