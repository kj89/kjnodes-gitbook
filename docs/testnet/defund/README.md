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
peers="ba0abf77c2dec230a7ae06b32d1abf63dbd48642@5.9.82.120:60656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,41605a6e5b6e22e349e67e8f9088ac93b958e104@45.94.58.246:40656,5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836,04ff1f98174b35960d8bc2d10bf0da1406f7028b@194.146.12.215:27656,f8093378e2e5e8fc313f9285e96e70a11e4b58d5@141.94.73.39:45656,230d474bebd608fa076c7ae2585a180fdc1befae@185.252.233.99:26656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,d0623f88f6960343f11d920ac72bfebf13179a8d@185.208.206.56:26656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,93153d3b1e9178f44bbbddf809a8cf7177715c03@37.221.71.67:45656,7a3c4079964eaca46f63f9a4ba37997ae55bee60@45.85.249.93:27656,6047d282f126e8be4b36ca28c0cc3d244577f798@159.69.185.109:26656,205f6826808509bb8be87bfff953dd422bfff962@207.180.254.16:28656,ffb2898494cdbd6625d962ea4511c29507177c62@164.68.103.176:26656,8a650a9761db8abc1096abc3d4a68431600ae835@62.171.149.101:46656,195f80fa7d564efd62304bcb7da85f0a50f3d7db@109.123.254.113:26656,15a7590aef64d07b825f9f31d46582ce0c6aa6ca@82.208.23.194:26656,1a8e8d6667615f4836c1c1403563a26a1044fd00@116.203.158.189:26656,868120d57a36f8fbaba2cb8d3bab15759f8bab64@5.199.136.44:40656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,28e18559a10e257e80a79730731fe3d0d03a8f52@79.137.248.29:40656,4598cef0683d229c628702180959721eba8c598b@142.132.253.112:18656,790d14b181c9f538bfa81afaf70fe78c3e9b52e2@38.242.199.69:26656,ccebeed4dae0fe100826f7c7c111d4d62c4bb546@109.123.240.111:27656,af9f3f65b3082007020697d035e7d5031e3be25b@212.23.222.89:26656,d1c8bfe892396220d19c8815dcc4e536aaf0e080@164.68.127.58:26656,278602404e78c23f5aff7a04802179ad7ffaa676@18.234.102.132:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
