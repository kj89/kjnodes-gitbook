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
peers="89d4b6b28f4399f49c82f9b0e891463f07f26cfe@95.216.65.177:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,1e839449cac1898e98901a7d2c216c1a608c4e20@65.21.203.204:18656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,37cbd04b4608dc4b83aa4b755c6b2f3e90b4ca13@149.102.140.94:26656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,18163407ab3a5045cd094f8e546e2732fcd53d32@45.8.132.82:26656,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,1cb8223111a5fb8a631d73aa3bcd7abd2ef41ba7@45.87.104.84:1184,7c2ea36064077da73d0ad5b60d8ef215acbee50b@161.97.79.100:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,b4553ec94efe9cb11c684661042eedc2adf6ead3@23.88.74.54:42656,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
