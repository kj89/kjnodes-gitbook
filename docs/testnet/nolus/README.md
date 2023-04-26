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
peers="7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,ce24c9afeb996856a32673b0ee378ee09c066ebe@217.76.48.63:38656,0760923eff6e1e890a55e3c3d6b1330d60c2f870@185.246.86.152:26656,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,2e80da0046dd3f2205a207dd435b6c9b0f9bfc04@65.109.93.152:27656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,e6b3d520d342782129689d5f9aee6c8f12933a61@51.89.7.235:26649,1a5f37caaa5dd174bc2797bf2a70b804e71bc632@162.55.42.27:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,d95efc810d8519321816047670b3032db07ac6ee@91.229.245.219:26656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,1d560eb80e578546285871dc31a8e58828635c0e@65.109.65.163:20756,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,38e75806248cd215e1e71d94e3db8c08bcf87702@95.214.55.138:27656,ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,785789b6574c45b8cfefff08344fdfeda345c7e1@135.125.5.34:55666,65cc76edf50ee3cf7a93539f39067d1ed6be1e6d@65.108.224.156:26656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,b8ab798f77c0276d245c4f095d502d7107f484b9@138.201.204.5:26656,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,4d8aed7bff4156c62ebb4f787e06d5d45d681b76@109.111.160.171:34656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
