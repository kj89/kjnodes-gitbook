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

**live-peers** (23)
```bash
peers="15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,f50302cde48497a2af29168c23c530299116fd84@89.252.21.37:36656,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,73e55e512de96e81fa025463f1581daf64172f76@65.108.13.154:31656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,441ee01f2bb396bf4116f197e4d9eefbd88f5e10@65.109.122.105:60756,538e2a3d6e96cd7bc0635eaa3f8f3695f26503a7@65.108.104.167:21656,87e0efe332fdc4b0c2a76d18761a936509762067@212.41.9.98:36656,37933575674b670c91a6aa336b1dd910057465a9@157.90.208.222:60556,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,8f767a425f5c6de20ffc435154c6351d118b806e@207.180.243.64:46656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,cdfcaee60fe31b33a32929a3e15d02f8e2508f98@135.181.160.61:31656,1c50df97e155afa50189f48daf41be046c7fe682@85.10.202.135:32656,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
