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
peers="627d906b9c112752d153e87dfa9925730f6a7414@95.217.105.54:13656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,9f8028ece9c514cf8f2646f8d968480b3341149f@157.90.25.62:26656,31cd6288a8fa2c9caa191fbddef0301ca0e04881@194.163.177.203:26656,23c52b4aa95a5b269277292410f6f4c8815e616c@194.163.174.103:27656,5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836,790d14b181c9f538bfa81afaf70fe78c3e9b52e2@38.242.199.69:26656,dfa7af21b8c6efebe8aa6028196324f9e0540bbc@94.130.55.76:39656,db8ea4712b47f5d6a19e942977a2e82daacf127f@88.99.115.105:13656,ea6f307baa6c66fcd565ae25692d40aca61b17fc@148.251.123.151:13656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,905cf74e6c4df9d4894f134c821d1399a4da547f@109.123.250.128:26656,04ff1f98174b35960d8bc2d10bf0da1406f7028b@194.146.12.215:27656,b695113e075d522271c41ccb57b0a2c27e8ae346@65.109.160.32:40656,7a3c4079964eaca46f63f9a4ba37997ae55bee60@45.85.249.93:27656,6b8021f2cf9bdad927473dd6cb075a83787a268a@89.179.33.100:26656,8a5cc818253b02eb408314ea1b5ff4788cc6e7a1@65.109.65.248:33656,230d474bebd608fa076c7ae2585a180fdc1befae@185.252.233.99:26656,0a03781fa64c2f2810cbbaacb81418170f53fe13@45.88.188.253:26656,ffb2898494cdbd6625d962ea4511c29507177c62@164.68.103.176:26656,b0018ac03d48edb02a82bb92429cbe3fc75c58b1@161.97.172.129:26656,ae95d629c68b76c7a0f7695b2e63e6c5464ec435@212.90.120.12:27656,bc934501cffc27940d96e7775b6b8ae5122604ab@185.185.80.195:28656,e494f017a60c9be7b73541ea9356affbeee1c9cb@178.18.247.73:27656,868120d57a36f8fbaba2cb8d3bab15759f8bab64@5.199.136.44:40656,cdcd6ba08042b31391492666da593cc80d198cab@84.54.23.85:26656,c1c6cf5859c43fb3acd19ccdb78a4caa0a151ff7@45.85.249.107:27656,eb7040eb80f3a0b62df828d38d818b3aec554b50@38.242.237.125:26456,b654f4b9394fcb6a98ca5845c70bb4026aa34fda@209.145.62.91:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
