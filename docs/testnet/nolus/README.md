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

**live-peers** (30)
```bash
peers="ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,0760923eff6e1e890a55e3c3d6b1330d60c2f870@185.246.86.152:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,785789b6574c45b8cfefff08344fdfeda345c7e1@135.125.5.34:55666,2e80da0046dd3f2205a207dd435b6c9b0f9bfc04@65.109.93.152:27656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,1a6e1ad836c993a1a33e7923a5387acdd1c9b590@65.109.90.171:31656,4aaa12410714e59a6d9af52ae0cf95c6e42af0ba@65.108.199.120:61456,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,228b1139c787fcb02358d99db748119123cf08c0@65.109.65.163:20756,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,a95975f3a58e20ba1c518f3cbb1c23ef7569e4d4@14.241.82.87:26656,7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,2e146ac9281e3797cbe1ad053e5ce6046b972c15@65.109.140.29:37656,003a270b5085d8c14a075abc1ac3699f34161e49@185.248.24.224:37656,4cf9c28f20faac9baae74870cb52bae590dbd81e@65.108.228.96:26656,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,1a5f37caaa5dd174bc2797bf2a70b804e71bc632@162.55.42.27:26656,4d8aed7bff4156c62ebb4f787e06d5d45d681b76@109.111.160.171:34656,300509c4c52a00fac5a1f3ec0573e44eaa9f22b9@173.212.223.233:26656,56cee116ac477689df3b4d86cea5e49cfb450dda@54.246.232.38:26656,e84c51a539d705787644e235faab6bccd4b73bdd@5.61.33.18:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
