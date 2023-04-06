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

**live-peers** (26)
```bash
peers="1a5f37caaa5dd174bc2797bf2a70b804e71bc632@162.55.42.27:26656,37933575674b670c91a6aa336b1dd910057465a9@157.90.208.222:60556,f0f48327e14e6918a2fad2c795429dd6c3856236@88.99.161.162:43656,ac86c1678e20a87bf2f036741932910869726337@135.181.222.185:15656,b707384941f6ae2c291d7031b51771c470e3a686@65.108.9.230:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,72ccd1176df36fb799e14721639e21b1ec360f0a@65.108.9.164:20756,89d4b6b28f4399f49c82f9b0e891463f07f26cfe@95.216.65.177:29656,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,91197362c5949e7c512783cd8e71b132551b1b2c@89.117.57.201:13656,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,43b2582d9f63b46df12879729e8d3d1daa899ef4@144.126.154.230:26656,300509c4c52a00fac5a1f3ec0573e44eaa9f22b9@173.212.223.233:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,896c70ce52e6c88313048c9a63fcb9e7f0277144@178.208.86.44:46656,ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,b8ab798f77c0276d245c4f095d502d7107f484b9@138.201.204.5:26656,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
