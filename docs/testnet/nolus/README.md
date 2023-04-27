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

**live-peers** (30)
```bash
peers="ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,1d560eb80e578546285871dc31a8e58828635c0e@65.109.65.163:20756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,a12f0c225332ab006fbc46d58706669bf44f52e0@113.176.160.117:26656,17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,73176af073e4f89609db7aa4ec3561ce1b98d308@85.10.193.246:32656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,c2e461ef97ce664bc1e91ea95ecaa8766f58ce88@65.109.116.110:26656,4aaa12410714e59a6d9af52ae0cf95c6e42af0ba@65.108.199.120:61456,e6b3d520d342782129689d5f9aee6c8f12933a61@51.89.7.235:26649,b2405df829289167d99262d5f3125f13972ea6e1@14.238.7.59:26656,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,65cc76edf50ee3cf7a93539f39067d1ed6be1e6d@65.108.224.156:26656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,73e55e512de96e81fa025463f1581daf64172f76@65.108.13.154:31656,0760923eff6e1e890a55e3c3d6b1330d60c2f870@185.246.86.152:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,eecb12ab9e15bdf74a73497bc177c85e2f5161d6@38.242.207.216:26656,38e75806248cd215e1e71d94e3db8c08bcf87702@95.214.55.138:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
