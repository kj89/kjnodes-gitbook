# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.2.2-store-fix | **Wasm**: ON

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
peers="ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,228b1139c787fcb02358d99db748119123cf08c0@65.109.65.163:20756,1c50df97e155afa50189f48daf41be046c7fe682@85.10.202.135:32656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,e84c51a539d705787644e235faab6bccd4b73bdd@5.61.33.18:26656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,aad36d817f6f5c66a002b87a4fb133a3e3137b31@194.163.187.175:43656,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,f50302cde48497a2af29168c23c530299116fd84@89.252.21.37:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
