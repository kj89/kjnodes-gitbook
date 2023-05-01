# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.2.2-equalize-store-heights | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nolus-testnet](https://explorer.kjnodes.com/nolus-testnet)

## Public endpoints

* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)
* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* grpc: nolus-testnet.grpc.kjnodes.com:143090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:143656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:143659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (24)
```bash
peers="0760923eff6e1e890a55e3c3d6b1330d60c2f870@185.246.86.152:26656,7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,1d560eb80e578546285871dc31a8e58828635c0e@65.109.65.163:20756,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,a12f0c225332ab006fbc46d58706669bf44f52e0@113.176.160.117:26656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,f50302cde48497a2af29168c23c530299116fd84@89.252.21.37:36656,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,65cc76edf50ee3cf7a93539f39067d1ed6be1e6d@65.108.224.156:26656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,73176af073e4f89609db7aa4ec3561ce1b98d308@85.10.193.246:32656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,2fc6d24d1d77c34427ce7cbb24de5ee4d4debe7c@161.97.108.208:26656,7cbd276b062030802fc7efb18b10a565c4fb88a5@92.50.75.81:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
