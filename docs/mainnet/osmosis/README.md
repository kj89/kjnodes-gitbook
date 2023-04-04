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

**live-peers** (30)
```bash
peers="57eb30061f595699185f3161925827bb5a391264@195.154.200.69:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,4c927f93d430baf31e6d6418e62c56f442f092bc@46.4.28.42:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,ec929701754be057fb38c824fc127e26add9c900@138.201.121.185:26666,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,069922fc087982553f10d9e6163948d0d6dfecb4@65.109.28.58:26656,b54d611ce10b7a4e816fae4e0b87b44f25c7da74@50.242.73.9:26656,9bdeb59c97c139187236b2ce92c229c3b9156d93@5.78.80.161:26656,4d2605490fcd7369800cb0e1e27ef6d433c1cd96@65.109.20.37:26656,e327b773177d3a00c461f59552a1962dd83741b2@65.108.9.164:10156,c29b58aa25198ef724189f9a0b8d7ef4399d9587@65.109.52.178:26656,3e3f8f3a9ed941600550d090900aee639abb7906@93.159.134.158:56656,e3ab699881792abe822e6de3a0da6eb84a143903@34.79.77.122:26656,91ed0275dcc075ba506a150b446f32ca38d805e0@195.14.6.2:26656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,2186d344ff775c8181bf31de600eed0c72b9fe9e@65.109.28.213:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,a559df67d051d54627a3e25584ff18b8ca55a8b0@95.216.46.251:26656,7c5459ea4bbc41aa4d86ffe8126f0651155227c8@85.195.102.127:26656,63b4a45bb2276fe141e69ce83750a2c53f1ceeda@198.244.202.196:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
