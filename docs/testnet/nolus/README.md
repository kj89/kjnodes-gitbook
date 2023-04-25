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

**live-peers** (27)
```bash
peers="4aaa12410714e59a6d9af52ae0cf95c6e42af0ba@65.108.199.120:61456,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,1a6e1ad836c993a1a33e7923a5387acdd1c9b590@65.109.90.171:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,0a7ece014d1dbffe5bc0b7a9f5399573ac8a335d@144.91.92.219:26656,7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,73e55e512de96e81fa025463f1581daf64172f76@65.108.13.154:31656,b04b320e306ccd38b3da4d5ebc8099ceff452c65@178.63.8.245:61456,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,2e146ac9281e3797cbe1ad053e5ce6046b972c15@65.109.140.29:37656,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,65cc76edf50ee3cf7a93539f39067d1ed6be1e6d@65.108.224.156:26656,73176af073e4f89609db7aa4ec3561ce1b98d308@85.10.193.246:32656,56f14005119e17ffb4ef3091886e6f7efd375bfd@34.241.107.0:26656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,a95975f3a58e20ba1c518f3cbb1c23ef7569e4d4@14.241.82.87:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
