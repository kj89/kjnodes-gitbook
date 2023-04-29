# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.2.2-equalize-store-heights | **Wasm**: ON

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

**live-peers** (24)
```bash
peers="73e55e512de96e81fa025463f1581daf64172f76@65.108.13.154:31656,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,73176af073e4f89609db7aa4ec3561ce1b98d308@85.10.193.246:32656,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,1d560eb80e578546285871dc31a8e58828635c0e@65.109.65.163:20756,1a6e1ad836c993a1a33e7923a5387acdd1c9b590@65.109.90.171:31656,e6b3d520d342782129689d5f9aee6c8f12933a61@51.89.7.235:26649,ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,f50302cde48497a2af29168c23c530299116fd84@89.252.21.37:36656,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,a12f0c225332ab006fbc46d58706669bf44f52e0@113.176.160.117:26656,65cc76edf50ee3cf7a93539f39067d1ed6be1e6d@65.108.224.156:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,b2405df829289167d99262d5f3125f13972ea6e1@14.238.7.59:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
