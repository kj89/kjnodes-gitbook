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

**live-peers** (30)
```bash
peers="f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,127b4bca7027bd677d342eed279acbdbe52832c5@178.18.245.137:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,790d14b181c9f538bfa81afaf70fe78c3e9b52e2@38.242.199.69:26656,205f6826808509bb8be87bfff953dd422bfff962@207.180.254.16:28656,eb7040eb80f3a0b62df828d38d818b3aec554b50@38.242.237.125:26456,dca0e42d5d6838954ae08b5526c42a80c01d5538@159.69.74.237:26756,d0623f88f6960343f11d920ac72bfebf13179a8d@185.208.206.56:26656,868120d57a36f8fbaba2cb8d3bab15759f8bab64@5.199.136.44:40656,c659b2e0ec4027e6d4977c49917bdbd27451203f@130.185.119.129:26656,230d474bebd608fa076c7ae2585a180fdc1befae@185.252.233.99:26656,ccebeed4dae0fe100826f7c7c111d4d62c4bb546@109.123.240.111:27656,ffb2898494cdbd6625d962ea4511c29507177c62@164.68.103.176:26656,bc3d614b684c8e1647f4196dc8a785b1ab0381ef@65.108.13.154:33656,e494f017a60c9be7b73541ea9356affbeee1c9cb@178.18.247.73:27656,d1c8bfe892396220d19c8815dcc4e536aaf0e080@164.68.127.58:26656,af0aee9f4b50d9ea30b64be0ab78415824ab87c7@65.21.237.241:26656,7a3c4079964eaca46f63f9a4ba37997ae55bee60@45.85.249.93:27656,8c48e2b5498ec307aafabb3a6887bd4bf68e5457@65.108.140.109:33656,bb76da2dd5d971ca420f1a72244158b4db9c0373@82.208.23.192:26656,f8093378e2e5e8fc313f9285e96e70a11e4b58d5@141.94.73.39:45656,5ce286faea0eb730e6d4f3636ab572fea20a879d@86.48.5.92:27656,04ff1f98174b35960d8bc2d10bf0da1406f7028b@194.146.12.215:27656,e67677fb5532cde14575e33c2bf4b1ed5b3e6bc3@116.202.117.229:33656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,cdadad3c8fc2982484fe7fd4fd041dcd437c6f8e@116.202.225.84:13656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,8b80bc13d578d4e80fd672c247491f917c26a71d@84.201.162.168:26656,ea1af576f728832d90d4fe9944e45743bb270f24@154.12.245.40:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
