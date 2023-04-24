# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.2.2-store-fix | **Wasm**: ON

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
peers="e6b3d520d342782129689d5f9aee6c8f12933a61@51.89.7.235:26649,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,37933575674b670c91a6aa336b1dd910057465a9@157.90.208.222:60556,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,228b1139c787fcb02358d99db748119123cf08c0@65.109.65.163:20756,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,65cc76edf50ee3cf7a93539f39067d1ed6be1e6d@65.108.224.156:26656,0760923eff6e1e890a55e3c3d6b1330d60c2f870@185.246.86.152:26656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,e4b7228ccadf3180e6e323aa4c0c97946ac054dc@65.109.112.20:11134,22acc593150fc38f9b1a2dc93cdc05e22566e7f6@213.239.207.165:29856,7c2ea36064077da73d0ad5b60d8ef215acbee50b@161.97.79.100:36656,73e55e512de96e81fa025463f1581daf64172f76@65.108.13.154:31656,2e80da0046dd3f2205a207dd435b6c9b0f9bfc04@65.109.93.152:27656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,78988c94a1a8f37b8995c7794d103e2979cefd2e@5.75.231.119:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
