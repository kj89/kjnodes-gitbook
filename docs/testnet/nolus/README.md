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

**live-peers** (25)
```bash
peers="ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,1d560eb80e578546285871dc31a8e58828635c0e@65.109.65.163:20756,ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,f50302cde48497a2af29168c23c530299116fd84@89.252.21.37:36656,dba152eadb37e427969c2bd8b6a31e930879f571@152.70.188.61:26656,7c2ea36064077da73d0ad5b60d8ef215acbee50b@161.97.79.100:36656,18163407ab3a5045cd094f8e546e2732fcd53d32@45.8.132.82:26656,2fc6d24d1d77c34427ce7cbb24de5ee4d4debe7c@161.97.108.208:26656,b8ab798f77c0276d245c4f095d502d7107f484b9@138.201.204.5:26656,85fa33f8bac6dd4d7e8aa6dff5c8eb8d9019128e@24.207.176.67:26776,e6b3d520d342782129689d5f9aee6c8f12933a61@51.89.7.235:26649,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
