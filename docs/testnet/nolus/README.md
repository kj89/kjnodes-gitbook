# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.2.2 | **Wasm**: ON

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
peers="ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,72ccd1176df36fb799e14721639e21b1ec360f0a@65.108.9.164:20756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,6cb8e63bf00d37399454ab24b6cf316062b90117@199.175.98.110:36656,17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,0760923eff6e1e890a55e3c3d6b1330d60c2f870@185.246.86.152:26656,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,785789b6574c45b8cfefff08344fdfeda345c7e1@135.125.5.34:55666,4d8aed7bff4156c62ebb4f787e06d5d45d681b76@109.111.160.171:34656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,e6815712c11d21d3fed33c80c49f416bc8f186ae@165.232.74.22:26656,b8ab798f77c0276d245c4f095d502d7107f484b9@138.201.204.5:26656,201bfc79e581623df3e504c5aca19f06fde44e20@144.91.70.120:31656,1b3d3ab6b77de33c3ab193c5f1a3e42e946acc7f@65.109.88.251:11006,367fb20ca2380ebbb73eb19b772564383b0f37ee@65.21.123.172:26656,89aaf76a23b16bd57a1982e7b304fd998a49942a@65.109.85.226:9000,8d59cbd6f8aa5c19613b1e64560f6024cde2ef81@202.61.251.135:26656,cdfcaee60fe31b33a32929a3e15d02f8e2508f98@135.181.160.61:31656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,003a270b5085d8c14a075abc1ac3699f34161e49@185.248.24.224:37656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,4cf9c28f20faac9baae74870cb52bae590dbd81e@65.108.228.96:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
