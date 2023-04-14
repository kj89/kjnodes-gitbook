# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: orbit-alpha-1 | **Latest Version Tag**: v0.2.6 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: defund-testnet.grpc.kjnodes.com:40090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (29)
```bash
peers="d0623f88f6960343f11d920ac72bfebf13179a8d@185.208.206.56:26656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,7a3c4079964eaca46f63f9a4ba37997ae55bee60@45.85.249.93:27656,04ff1f98174b35960d8bc2d10bf0da1406f7028b@194.146.12.215:27656,c9dc9d0ddcd9aba39353c77f03168a85912849e3@65.108.200.40:33656,ffb2898494cdbd6625d962ea4511c29507177c62@164.68.103.176:26656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,0a03781fa64c2f2810cbbaacb81418170f53fe13@45.88.188.253:26656,230d474bebd608fa076c7ae2585a180fdc1befae@185.252.233.99:26656,dca0e42d5d6838954ae08b5526c42a80c01d5538@159.69.74.237:26756,205f6826808509bb8be87bfff953dd422bfff962@207.180.254.16:28656,af0aee9f4b50d9ea30b64be0ab78415824ab87c7@65.21.237.241:26656,fdeae2b0bf494c8e2b7b95c8639833e76c3e3d14@95.165.31.167:40656,eb7040eb80f3a0b62df828d38d818b3aec554b50@38.242.237.125:26456,bb76da2dd5d971ca420f1a72244158b4db9c0373@82.208.23.192:26656,bc3d614b684c8e1647f4196dc8a785b1ab0381ef@65.108.13.154:33656,cdadad3c8fc2982484fe7fd4fd041dcd437c6f8e@116.202.225.84:13656,b695113e075d522271c41ccb57b0a2c27e8ae346@65.109.160.32:40656,912d95a925bb827e1f6ac08810742d658fd2268e@185.218.126.186:27656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,a79130668102f116a23cfcf9fd94623de4a223fe@81.30.157.35:10656,cf94df3ec5c7eca271a1d59b335ae743b2e0307d@185.215.167.45:26656,6999cca6c55576a48d4f227b87dc904fbdb085aa@65.21.134.202:26576,8c48e2b5498ec307aafabb3a6887bd4bf68e5457@65.108.140.109:33656,54315866e9a9c0bd7611a42a1caaf4a244316eb3@65.108.200.60:13656,86cf7d0916950d2b48294ed6106f045a7b25aec7@77.105.137.135:26656,f05be2e85cb0cd1a5a5a6837b217d39c05dacf75@65.108.232.174:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,af9f3f65b3082007020697d035e7d5031e3be25b@212.23.222.89:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
