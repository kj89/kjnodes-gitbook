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
peers="acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,37933575674b670c91a6aa336b1dd910057465a9@157.90.208.222:60556,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,53156633e3dbfe2e514fa0676c1d42f046d9ca40@65.108.129.29:26656,441ee01f2bb396bf4116f197e4d9eefbd88f5e10@65.109.122.105:60756,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,b707384941f6ae2c291d7031b51771c470e3a686@65.108.9.230:28656,dba152eadb37e427969c2bd8b6a31e930879f571@152.70.188.61:26656,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,7f26067679b4323496319fda007a279b52387d77@63.35.222.83:26656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,b8ab798f77c0276d245c4f095d502d7107f484b9@138.201.204.5:26656,785789b6574c45b8cfefff08344fdfeda345c7e1@135.125.5.34:55666,8f767a425f5c6de20ffc435154c6351d118b806e@207.180.243.64:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,ca83b6457bfce88d892646b6afb51165ec3e94d4@135.181.183.93:22656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
