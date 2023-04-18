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

**live-peers** (28)
```bash
peers="ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,f7af30d030da2dd7a0a369997eafa1bdb4f53e75@83.11.99.192:24656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,228b1139c787fcb02358d99db748119123cf08c0@65.109.65.163:20756,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,2fc6d24d1d77c34427ce7cbb24de5ee4d4debe7c@161.97.108.208:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,0760923eff6e1e890a55e3c3d6b1330d60c2f870@185.246.86.152:26656,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,538e2a3d6e96cd7bc0635eaa3f8f3695f26503a7@65.108.104.167:21656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,052dfbd088acc98fef7c42efc04a4ef6e8999ee3@65.109.117.165:43656,1e839449cac1898e98901a7d2c216c1a608c4e20@65.21.203.204:18656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,e6b3d520d342782129689d5f9aee6c8f12933a61@51.89.7.235:26649,a12f0c225332ab006fbc46d58706669bf44f52e0@113.176.160.117:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
