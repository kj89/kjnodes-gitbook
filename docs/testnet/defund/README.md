# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-4 | **Latest Version Tag**: v0.2.2 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: [https://defund-testnet.grpc.kjnodes.com](https://defund-testnet.grpc.kjnodes.com)

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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,f8093378e2e5e8fc313f9285e96e70a11e4b58d5@141.94.73.39:45656,a56c51d7a130f33ffa2965a60bee938e7a60c01f@142.132.158.4:10656,28f14b89d10992cff60cbe98d4cd1cf84b1d2c60@88.99.214.188:26656,c1d2c7a810c386595e59ead21ba69555a37ac007@5.161.110.128:26656,72ab81b6ba22876fc7f868b58efecb05ffac9753@65.109.86.236:28656,2b76e96658f5e5a5130bc96d63f016073579b72d@51.91.215.40:45656,01b73409f0a44e9998af038259ce079af906c405@65.109.167.54:26656,e26b814071e94d27aa5b23a8548d69c45221fe28@135.181.16.252:26656,11dd3e4614218bf584b6134148e2f8afae607d93@142.132.231.118:26656,4eb0bef7997b87086c40766193d812479238187c@217.76.55.66:26656,a9c52398d4ea4b3303923e2933990f688c593bd8@157.90.208.222:36656,8ce02398652b4f4c953280ecd21949c4cf4a1414@167.86.105.64:26656,22f39b636c4984d658061788609305b3dc87f3ac@165.232.176.176:26656,47a6af2b45c2a8af64b36b4730bfb3d0c91ed870@88.210.3.84:26656,fadb50dd153e127fbd56b7a4823beb355d4c103b@217.76.55.73:26656,514d7a0dc5c5ab4df2269e106f02554763a0cd69@88.210.9.169:26656,28d0f4d4b9debc4547e8d7862672171e7b2f8764@135.181.111.161:26656,164e549bcddbfee83fe19810b645e80cac1b358d@65.109.12.79:26656,20045ce5bdc8fbc356d82351305fe2f9f188a4b5@217.76.55.68:26656,7df04198931e556de89a8400a52e4fe8fc8bdfe3@65.108.60.172:26656,0f332b3b2e0013d3a52bcf0d85871e510628c90f@193.178.170.14:26656,9389cefdaa999eb81b93f4354d1077553ceb7a86@217.76.55.76:26656,611fa8f9e30b531d12d517c2dd89eae132057c8b@217.76.55.69:26656,c1b574a8230bb51a6d1ae74071659ecdae1e968d@217.76.55.67:26656,733cfe295420fc7a7c03e137a807021b3b74c6ff@135.181.199.127:26656,d31d9801e7a021d287570b94ffcf27b91b0d9b66@217.76.55.74:26656,2a138efb5ef0638386af44c3df32ccdc8895b4d0@65.21.172.60:36656,a629ef8303b7bb7b938c566c4d0c13d60653e83b@65.108.126.35:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
