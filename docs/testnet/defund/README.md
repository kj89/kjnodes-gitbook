# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (30)
```
peers="175cdc1cae6635d5779e8870a20f761f1d58f02f@65.109.51.41:36656,71663397bb1d94d1b58af63cc2a0111bcabf01b9@65.109.82.75:26656,0b141f72551552a5faf109413292e72408a34c34@65.109.27.156:32656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,bd90b1dd4ae3636e5f452be51b8e75ca104b5bfc@109.123.247.53:40656,4135c03053c6f02e4ca773bee42d5c7f62922566@185.217.125.238:26656,0a1fcc2907e50b46f021389049c79f7d124f9946@77.51.200.79:36656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,aee64a0d9b4f06f9f0949650fa22494b1cee1d58@84.46.244.228:26656,748e7c000dc2fe6ac66686884f8533fc7916b6a3@38.242.244.163:26656,544266471d3da917f0b6cf3b65f9d437d62134e8@157.90.252.194:26666,f4869f02f970f222d81718a7a2fcf9b3c7b1b10c@109.123.249.189:26656,98a777dad655ddfbca503742107ff63fc5e0a9f5@45.147.199.212:26656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656,e104f008f6d1227170d3b4ce1d73f0ea2068094f@84.201.162.168:26656,18921a27facf3760d59147e4ae176b1bdf226346@195.201.237.172:18656,f329bee02e530e05a8937887c8ea4e75851281f1@194.180.176.126:26656,5e6354412f3742ac76e37838236707b373c1de43@185.250.37.162:29656,d1976601f04df2a2c7e35c0e8212464acfb7512e@75.119.147.235:26656,68b4a53b3b67da6a4736888c36074eb316ea510d@75.119.157.222:26656,53e2240528947ff8f7b037d347b7258f05ce88f0@89.179.68.98:27656,f868bc6debc472df810792e22ebeeb8d8e95f094@89.58.45.204:60756,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,dc8661d36681b73cf4dfde1d68587aec88212344@154.12.225.113:40656,4d3b782ab389525370f53d40e970b1362bc92106@185.182.186.202:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,8a650a9761db8abc1096abc3d4a68431600ae835@62.171.149.101:46656,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656,e4470dac98f2cee5bd060c52c7d801d57bfc9308@185.245.182.206:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
