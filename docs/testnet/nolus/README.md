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

**live-peers** (25)
```bash
peers="acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,367fb20ca2380ebbb73eb19b772564383b0f37ee@65.21.123.172:26656,2e80da0046dd3f2205a207dd435b6c9b0f9bfc04@65.109.93.152:27656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,538e2a3d6e96cd7bc0635eaa3f8f3695f26503a7@65.108.104.167:21656,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,f50302cde48497a2af29168c23c530299116fd84@89.252.21.37:36656,60c57c5b7215c84260249768cf66ae550142af9f@141.98.169.25:26656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,fa0a2fe57c2ab28aee6cc0be4eddbc68d6587a75@95.217.165.189:26656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,8d85b69ea7175ce0cf6ec7badae239339d6525db@81.0.218.59:26656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,ac86c1678e20a87bf2f036741932910869726337@135.181.222.185:15656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
