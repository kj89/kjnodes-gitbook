# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

Website: [https://www.defund.app](https://www.defund.app)


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

**live-peers** (29)
```
peers="e3d98694b276a2fa3bd52a77d00d379f0aacb58c@173.249.7.166:26656,92ea21c6dfc2fe2cc0315948cf5782888ae3bc28@62.171.129.168:26656,bd4c137c54e4856b2d59d77dbd52b57e0fb7529e@149.102.152.61:26656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,07f9db50ae2795727a09668d75b72cae285335d1@198.244.200.221:26656,cf6b23f9ceadf7944fc8b89a7fb771d9caa6f431@65.21.3.95:26656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,18921a27facf3760d59147e4ae176b1bdf226346@195.201.237.172:18656,f8e7b1b8382b9d4b0c04274826a89682ad4b5bfb@62.171.143.40:26656,ad35b87df11c37b5f66931cd86c5dc2853aabae2@95.216.69.88:36656,7df51b9f8ec9405fddb7c35b534a70fe70f6b93e@194.163.191.80:26656,4d3b782ab389525370f53d40e970b1362bc92106@185.182.186.202:26656,4f865b04ff70dd314c840bb3c324f41edbb3c3ff@164.68.102.102:26656,fd2122d21e10253a86739bdd33686065008926ed@85.10.200.221:29656,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656,0a8430b93bd3ddbf247388ca638512981ff07eaf@195.3.220.9:26656,175cdc1cae6635d5779e8870a20f761f1d58f02f@65.109.51.41:36656,4758cb09f15174708880c0986bb0b57af4dc5d5d@135.181.208.169:27656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,0b141f72551552a5faf109413292e72408a34c34@65.109.27.156:32656,57eadf177e7429db82bfdbed6fa0521e8741e404@94.130.13.40:26656,06869237862f0d21266f2182f2dc4e4b319a0168@194.163.189.179:26656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,7ca31e50d5509104ea481869bcbe91e6883fe9d0@135.181.150.198:36656,d130db7a4901fd92a221f1cf7d006c6153751eb5@144.76.27.79:60956,0e5c41bec481ae4da0577377bc1952eb29b1e4c1@65.21.78.86:26656,98a777dad655ddfbca503742107ff63fc5e0a9f5@45.147.199.212:26656,27184beff22d064a593233bbe6b0883f9f7fc2ff@45.87.104.74:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
