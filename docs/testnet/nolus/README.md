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
peers="1a5f37caaa5dd174bc2797bf2a70b804e71bc632@162.55.42.27:26656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,fac035258738be9be98957d5d012d24841d2e5eb@85.10.197.4:16656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,a95975f3a58e20ba1c518f3cbb1c23ef7569e4d4@14.241.82.87:26656,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,87e0efe332fdc4b0c2a76d18761a936509762067@212.41.9.98:36656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,18163407ab3a5045cd094f8e546e2732fcd53d32@45.8.132.82:26656,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,a74d09de862f1ee4b8e41afcc59b70f0ce633b58@78.25.143.46:43656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
