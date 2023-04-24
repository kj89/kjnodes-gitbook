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

**live-peers** (29)
```bash
peers="acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,785789b6574c45b8cfefff08344fdfeda345c7e1@135.125.5.34:55666,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,228b1139c787fcb02358d99db748119123cf08c0@65.109.65.163:20756,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,054f9020746a61a41586a3b3750be684d1255520@75.119.154.2:43656,dba152eadb37e427969c2bd8b6a31e930879f571@152.70.188.61:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,a12f0c225332ab006fbc46d58706669bf44f52e0@113.176.160.117:26656,0760923eff6e1e890a55e3c3d6b1330d60c2f870@185.246.86.152:26656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,2e80da0046dd3f2205a207dd435b6c9b0f9bfc04@65.109.93.152:27656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,2e146ac9281e3797cbe1ad053e5ce6046b972c15@65.109.140.29:37656,1a6e1ad836c993a1a33e7923a5387acdd1c9b590@65.109.90.171:31656,7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,22acc593150fc38f9b1a2dc93cdc05e22566e7f6@213.239.207.165:29856,2fc6d24d1d77c34427ce7cbb24de5ee4d4debe7c@161.97.108.208:26656,65cc76edf50ee3cf7a93539f39067d1ed6be1e6d@65.108.224.156:26656,e84c51a539d705787644e235faab6bccd4b73bdd@5.61.33.18:26656,356a17fda44d7694cf8c3bf7a82491adea8536a9@38.242.228.69:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
