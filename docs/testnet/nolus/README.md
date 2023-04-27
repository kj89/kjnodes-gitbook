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
peers="37933575674b670c91a6aa336b1dd910057465a9@157.90.208.222:60556,ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,2fc6d24d1d77c34427ce7cbb24de5ee4d4debe7c@161.97.108.208:26656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,1d560eb80e578546285871dc31a8e58828635c0e@65.109.65.163:20756,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,65cc76edf50ee3cf7a93539f39067d1ed6be1e6d@65.108.224.156:26656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,ce24c9afeb996856a32673b0ee378ee09c066ebe@217.76.48.63:38656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,38e75806248cd215e1e71d94e3db8c08bcf87702@95.214.55.138:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,e6b3d520d342782129689d5f9aee6c8f12933a61@51.89.7.235:26649,c2e461ef97ce664bc1e91ea95ecaa8766f58ce88@65.109.116.110:26656,d95efc810d8519321816047670b3032db07ac6ee@91.229.245.219:26656,43e6a1f6f6d0d8d1fd7e7f8e13ca92ca3969433e@65.21.207.188:26656,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,dba152eadb37e427969c2bd8b6a31e930879f571@152.70.188.61:26656,0760923eff6e1e890a55e3c3d6b1330d60c2f870@185.246.86.152:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
