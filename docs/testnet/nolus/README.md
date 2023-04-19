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

**live-peers** (22)
```bash
peers="50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,228b1139c787fcb02358d99db748119123cf08c0@65.109.65.163:20756,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,ac86c1678e20a87bf2f036741932910869726337@135.181.222.185:15656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,785789b6574c45b8cfefff08344fdfeda345c7e1@135.125.5.34:55666,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,ca83b6457bfce88d892646b6afb51165ec3e94d4@135.181.183.93:22656,1e839449cac1898e98901a7d2c216c1a608c4e20@65.21.203.204:18656,2fc6d24d1d77c34427ce7cbb24de5ee4d4debe7c@161.97.108.208:26656,b707384941f6ae2c291d7031b51771c470e3a686@65.108.9.230:28656,ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
