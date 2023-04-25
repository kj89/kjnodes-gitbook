# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.2.2-equalize-store-heights | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nolus-testnet](https://explorer.kjnodes.com/nolus-testnet)

## Public endpoints

* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)
* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* grpc: nolus-testnet.grpc.kjnodes.com:43090

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

**live-peers** (29)
```bash
peers="65cc76edf50ee3cf7a93539f39067d1ed6be1e6d@65.108.224.156:26656,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,785789b6574c45b8cfefff08344fdfeda345c7e1@135.125.5.34:55666,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,1a5f37caaa5dd174bc2797bf2a70b804e71bc632@162.55.42.27:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,1d560eb80e578546285871dc31a8e58828635c0e@65.109.65.163:20756,b6c8dc38a5dba19a3f10d23b3572065db9265fa3@65.109.85.225:9000,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,d95efc810d8519321816047670b3032db07ac6ee@91.229.245.219:26656,1b3ca187a80b49baa789320ae5bded187c0bb6f9@217.76.54.184:36656,2fc6d24d1d77c34427ce7cbb24de5ee4d4debe7c@161.97.108.208:26656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,0a7ece014d1dbffe5bc0b7a9f5399573ac8a335d@144.91.92.219:26656,18163407ab3a5045cd094f8e546e2732fcd53d32@45.8.132.82:26656,f72ad216891e59cdc663958f55d2916e87c03c35@138.201.253.157:26666,17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,56f14005119e17ffb4ef3091886e6f7efd375bfd@34.241.107.0:26656,43454b0ce6e071ae04a211f1ad6104e303a84e10@43.207.171.121:43656,3413989cce29fa5913eb149cbdee4ea5ee02b579@194.34.232.124:55656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
