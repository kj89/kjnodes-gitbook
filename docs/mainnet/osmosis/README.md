# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:29090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:29656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:29659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (23)
```bash
peers="e5d1212f926d0da0de16e2fc4c0c4a2714a04ff4@18.159.135.176:26656,6178f129efa76d235436e2156959d0acb4772c6a@65.108.128.168:36656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,5696d9806c883beb725fb469d90039d921107b5b@116.202.209.186:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,287fc43ab0d194325290a6f3abd7c8e2e2867134@52.12.69.48:26656,8e72d0b37a9dc16ea58c0da705caa6530badd6ce@138.197.68.193:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,f95d9634ad68b8f0ac80ce308adb71d8c119ada5@141.98.219.104:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,27e14df66c9e4cd6b176b0dca6adfa9b6750f911@5.161.72.103:26656,ec929701754be057fb38c824fc127e26add9c900@138.201.121.185:26666,2d4ff3b8458bf1f9a127672738d3b7d1c9c107ca@3.15.176.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
