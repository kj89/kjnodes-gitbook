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

**live-peers** (29)
```bash
peers="5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,89d4b6b28f4399f49c82f9b0e891463f07f26cfe@95.216.65.177:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,228b1139c787fcb02358d99db748119123cf08c0@65.109.65.163:20756,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,fa0a2fe57c2ab28aee6cc0be4eddbc68d6587a75@95.217.165.189:26656,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,a95975f3a58e20ba1c518f3cbb1c23ef7569e4d4@14.241.82.87:26656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,5d65a11759b727862617c0fd5fa7f5e28ce4f41a@217.76.50.222:37656,298b24a95bf47f48ca091d82ddb31187baa4e920@162.55.1.176:26656,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,b4553ec94efe9cb11c684661042eedc2adf6ead3@23.88.74.54:42656,17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
