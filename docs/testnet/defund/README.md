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
peers="5b9504d6ba486791cee27e7d7aea247459c044ad@65.109.89.35:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@95.217.104.49:36656,cf94df3ec5c7eca271a1d59b335ae743b2e0307d@185.215.167.45:26656,74e6425e7ec76e6eaef92643b6181c42d5b8a3b8@65.108.231.124:18656,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,e0ab16d47276dee411fc01abc86c787d95ef6aba@65.109.111.204:29656,75e75e29076b44fed7e9d0236c59df1a8be4c3a6@65.21.91.248:13656,4f7ab0af137d148889a51a35463abebe268cd53a@199.247.4.188:40656,2218acbe81b1f57da84cf0db5ebb6fe65e5e3362@65.21.205.248:18656,88668b1252b6a1fe449f3d26ea8e761e75091863@154.53.55.91:30656,9f2087a5e238188451f515a8fc761c201167e2c7@65.21.245.170:26456,ee5ad3b44e90903d0bcecdbc0b4f16c4a3fa73d3@83.167.103.215:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836,d45d007633b82518764ab12fafa543c46c848e5d@88.99.213.25:40656,70a02b29719f2a3f7347e03aac2681af6c634f33@158.220.100.181:40656,9edc67cd8def17b8d09be3638fce62e420150a27@65.109.84.214:36656,7f33745f0c9ab289f1e202c70bea566dce27cf54@93.183.211.206:26656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,0eb9422efedd714d3db57d1ddfaad75f80a60518@5.161.99.35:26656,634ef7bf5c9619a68414ee87cf530132703e5d7b@144.76.97.251:29656,a3ede88696b2b5f752129889b84b9292a168133a@142.132.152.46:21656,d1649b67ea85b597064198f287414b9e3a93fa41@154.53.32.169:30656,8a5cc818253b02eb408314ea1b5ff4788cc6e7a1@65.109.65.248:33656,06c0fe8a5df43f71e88eaa3c07891338026ade9b@193.34.217.164:26656,d65109b0e823b26069be5ec255f84608fa98a100@89.163.213.61:40656,790d14b181c9f538bfa81afaf70fe78c3e9b52e2@38.242.199.69:26656,b654f4b9394fcb6a98ca5845c70bb4026aa34fda@209.145.62.91:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
