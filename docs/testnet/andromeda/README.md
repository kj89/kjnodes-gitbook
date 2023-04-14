# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:47090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (30)
```bash
peers="91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656,e2efe3e1d7e0ed2e5b6a1b384c47f745e9f205ac@65.108.141.109:31656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,cd3c6f22825b3208400558bd123009c9de0a636c@217.164.2.34:26656,7649ae1ea0dd5f640ac7dd7632a0866cf65e3aa4@31.220.90.78:26656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,200513402a2e1faf0b8ac5c7d3187ad4816c8c36@207.180.236.115:11656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,93e418796bf3b5d8cd319983269c99db83cb2ba6@5.161.78.48:16656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,85953732c4eb5165724ac6db331240ff0815daf1@1.15.104.210:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.20.220:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,27e8536dcd52c0ca8a733106a1e278255fe334d4@194.163.187.175:47656,41681200a0e60e9477181db813e1894684020378@194.233.92.77:26656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,5f7a675b1d496e73f71b3c69a909091dc49b8366@136.243.136.241:14656,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656,e48268700eb185984c0ab60b3cb14ca9e545fb4c@168.119.124.244:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,e8f8c97c65b3e65797eca3489de7c1682e85d4df@78.25.143.46:47656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,5cfce64114f98e29878567bdd1adbebe18670fc6@65.108.231.124:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
