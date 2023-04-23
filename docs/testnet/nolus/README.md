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

**live-peers** (30)
```bash
peers="73176af073e4f89609db7aa4ec3561ce1b98d308@85.10.193.246:32656,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,38e75806248cd215e1e71d94e3db8c08bcf87702@95.214.55.138:27656,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,85fa33f8bac6dd4d7e8aa6dff5c8eb8d9019128e@24.207.176.67:26776,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,228b1139c787fcb02358d99db748119123cf08c0@65.109.65.163:20756,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,56cee116ac477689df3b4d86cea5e49cfb450dda@54.246.232.38:26656,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,d95efc810d8519321816047670b3032db07ac6ee@91.229.245.219:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,c86c29f1118891b1543c14f5833e6f26e9231a10@213.246.39.53:36656,37cbd04b4608dc4b83aa4b755c6b2f3e90b4ca13@149.102.140.94:26656,2e146ac9281e3797cbe1ad053e5ce6046b972c15@65.109.140.29:37656,b04b320e306ccd38b3da4d5ebc8099ceff452c65@178.63.8.245:61456,60c57c5b7215c84260249768cf66ae550142af9f@141.98.169.25:26656,003a270b5085d8c14a075abc1ac3699f34161e49@185.248.24.224:37656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,e4b7228ccadf3180e6e323aa4c0c97946ac054dc@65.109.112.20:11134,dba152eadb37e427969c2bd8b6a31e930879f571@152.70.188.61:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
