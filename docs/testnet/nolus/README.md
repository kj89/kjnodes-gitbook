# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.2.1-testnet | **Wasm**: ON

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
peers="cd67fc6e6c306dbb863f381c926135d6b97fe685@65.109.85.155:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,84a5abdf6ce6f573ac1e3086ca693da6ec17c244@84.46.246.79:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,1c50df97e155afa50189f48daf41be046c7fe682@85.10.202.135:32656,538e2a3d6e96cd7bc0635eaa3f8f3695f26503a7@65.108.104.167:21656,8d85b69ea7175ce0cf6ec7badae239339d6525db@81.0.218.59:26656,2e146ac9281e3797cbe1ad053e5ce6046b972c15@65.109.140.29:37656,fa0a2fe57c2ab28aee6cc0be4eddbc68d6587a75@95.217.165.189:26656,dba152eadb37e427969c2bd8b6a31e930879f571@152.70.188.61:26656,367fb20ca2380ebbb73eb19b772564383b0f37ee@65.21.123.172:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,1e839449cac1898e98901a7d2c216c1a608c4e20@65.21.203.204:18656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,ac86c1678e20a87bf2f036741932910869726337@135.181.222.185:15656,c2e461ef97ce664bc1e91ea95ecaa8766f58ce88@65.109.116.110:26656,9f7560998c1bbced14d48261360746ce6cd09ec0@93.100.234.251:16656,3a0ca1d94b199af43ae28d32572dda8c5cc723d0@15.235.114.158:26656,8d86e527459e95ae31f2f02f0013d2f4c6bfdb91@65.109.81.119:37656,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,a83c42e544c0aebf978fd4283c8a99ddaf8f8e42@65.108.9.164:22956,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,472e6f38168746ef24f87467323e9ca02883ad24@66.206.2.162:30656,1825de8cabc89fddea10f1cf9d65eda46b0cc7a1@5.9.121.55:41956,87e0efe332fdc4b0c2a76d18761a936509762067@212.41.9.98:36656,8c431676468dbfb80e22cc4bfd3b7ef881a1198e@185.185.82.61:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
