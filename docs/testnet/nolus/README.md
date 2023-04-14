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
peers="46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,0760923eff6e1e890a55e3c3d6b1330d60c2f870@185.246.86.152:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,1e839449cac1898e98901a7d2c216c1a608c4e20@65.21.203.204:18656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,4aaa12410714e59a6d9af52ae0cf95c6e42af0ba@65.108.199.120:61456,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,538e2a3d6e96cd7bc0635eaa3f8f3695f26503a7@65.108.104.167:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
