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

**live-peers** (27)
```bash
peers="7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,60c57c5b7215c84260249768cf66ae550142af9f@141.98.169.25:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,2fc6d24d1d77c34427ce7cbb24de5ee4d4debe7c@161.97.108.208:26656,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,228b1139c787fcb02358d99db748119123cf08c0@65.109.65.163:20756,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,e6b3d520d342782129689d5f9aee6c8f12933a61@51.89.7.235:26649,7f5ce546e0ffec994995198e0a1b87caff61ae6d@178.18.253.102:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,65cc76edf50ee3cf7a93539f39067d1ed6be1e6d@65.108.224.156:26656,38d59fd3a6ff0047f368bbf5437ade8a76777d63@173.249.45.161:26656,ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,78988c94a1a8f37b8995c7794d103e2979cefd2e@5.75.231.119:26656,dba152eadb37e427969c2bd8b6a31e930879f571@152.70.188.61:26656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,e4b7228ccadf3180e6e323aa4c0c97946ac054dc@65.109.112.20:11134,a12f0c225332ab006fbc46d58706669bf44f52e0@113.176.160.117:26656,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,22acc593150fc38f9b1a2dc93cdc05e22566e7f6@213.239.207.165:29856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
