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

**live-peers** (28)
```bash
peers="ccebeed4dae0fe100826f7c7c111d4d62c4bb546@109.123.240.111:27656,4f1d96f5b8adb5bcdd59e61cb6e387ff12422a41@65.109.63.110:13656,230d474bebd608fa076c7ae2585a180fdc1befae@185.252.233.99:26656,790d14b181c9f538bfa81afaf70fe78c3e9b52e2@38.242.199.69:26656,eb7040eb80f3a0b62df828d38d818b3aec554b50@38.242.237.125:26456,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,ffb2898494cdbd6625d962ea4511c29507177c62@164.68.103.176:26656,41605a6e5b6e22e349e67e8f9088ac93b958e104@45.94.58.246:40656,6999cca6c55576a48d4f227b87dc904fbdb085aa@65.21.134.202:26576,251c53c762273adbb7853569d17af2a6f00e9c7a@65.108.101.124:13656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,2ea2700b0082d8d5bc9ed2f13b36af47cc787ea7@80.254.8.54:26656,354485ffcd96d2c292969fae86624f754924bb8c@91.77.165.172:28656,c659b2e0ec4027e6d4977c49917bdbd27451203f@130.185.119.129:26656,205f6826808509bb8be87bfff953dd422bfff962@207.180.254.16:28656,293806e54d286b72837723eebace872aea21c902@72.20.6.25:26656,86cf7d0916950d2b48294ed6106f045a7b25aec7@77.105.137.135:26656,65b7c9a6fa81e532e701e9179b890b3038a86962@149.102.136.186:27656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656,af0aee9f4b50d9ea30b64be0ab78415824ab87c7@65.21.237.241:26656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,969592457e566730a8894c04ab16e2018735d7ab@95.216.2.219:26656,9446504166663fc0090b81abdf86fafe93e72a40@185.209.30.95:40656,1a8e8d6667615f4836c1c1403563a26a1044fd00@116.203.158.189:26656,bc3d614b684c8e1647f4196dc8a785b1ab0381ef@65.108.13.154:33656,15a7590aef64d07b825f9f31d46582ce0c6aa6ca@82.208.23.194:26656,020abb71537ac87559814e1cb85cbd837046e836@23.88.5.169:23656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
