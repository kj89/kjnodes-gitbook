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

**live-peers** (30)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,0bc65a562eff399463fcf18f54716e32054e4cf4@188.166.88.185:26656,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,2e80da0046dd3f2205a207dd435b6c9b0f9bfc04@65.109.93.152:27656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,f77c45399c1dea69fcc48ff15995e8387169249a@80.85.242.54:26656,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,9f8e23a45a79ebd46abd47b916a51a47729c4df0@142.132.248.168:26656,e62dd608a302ba4f815a7cd3cf3d7facafa0e171@135.181.123.154:16656,e4b7228ccadf3180e6e323aa4c0c97946ac054dc@65.109.112.20:11134,395aec882a74ab9b679b1dc07df5f023b746bef6@85.190.246.119:26656,3cc31778757cdcf60f50cca61072aca40fd9f898@38.242.205.18:43656,56268f0d71ff5a6380ca82c2f741a240d6ec91da@45.151.122.213:26656,1278e67b0f6523c20e665109dd092ef20d6fd70e@45.67.230.23:26656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,5289137e6134895c5b3b82a9847869f2a889cdc0@65.108.97.58:2776,3be781c50aac85518bb3cfb8620528cbc5dacd67@146.190.45.222:26656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,c2c7344a10a39040592a8aa156ef9da17700d9a2@45.84.0.252:26656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,9e54327630e4f9668fb6137c5631c0ed6905b6e7@89.252.21.37:26656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,048df3fd3100c57b1a661aef3336a7c681657928@185.193.17.226:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
