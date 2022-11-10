# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.1.0

Website: [https://www.defund.app](https://www.defund.app)

## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Public peers

### state-sync

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

### seed-node

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```


## Address book
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

## Live peers (33)
```
PEERS="b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,d9d5f9a4ca3cb5ab7db0e6735b0ce8c246eceb6b@135.181.214.190:26656,75e38d35a430a9c1ac65249db3d4cab245159a8b@144.91.97.124:26656,26975c5bb7dc42463cc6361ea3c75f325e801917@5.161.86.214:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,3c838e2b140d36e08c406884ab75119c016c7938@159.69.217.0:18656,0f2d12d8a0cd0ce0c18b3c9701c5366ad6e48a65@178.128.219.172:40656,9f5a148876b9d51e1368fa491ebe1d35858b62a9@95.217.57.232:60556,d882fb5de964ed14acf84f2ed3f9e9fe00ece761@135.181.248.30:26656,9ae365f1c4a2b95c95fdcaa92db4a4f5a655ef1f@5.161.108.72:26656,36909ce5289d8f994fb2562f7a188a79ce826359@95.217.229.70:27656,867b72d6c8cbe690ae87eb32152cafa49484c6fd@65.109.32.174:27656,8190bf19ef96627e3b35f2039ab6aeed551fa05c@167.235.201.57:26656,ea0bfa100338b3016f0722bdd7b4d6c5eb22cb83@86.48.3.14:26656,028aa95415a9a004e57fd581d2c897f01a5b8054@80.241.211.235:26656,1fb99eb1ff6ad8e6be3f247f1a98cc9f7081e188@65.21.52.97:26656,f114c02efc5aa7ee3ee6733d806a1fae2fbfb66b@65.109.49.111:21656,17eb01fc972d963781b6666041fa164b3d5588e4@135.181.154.35:26656,117b4f356114c005714955ea6ee700fb6606c650@65.108.230.245:27656,015b3e38b3eccc7d3815e951e73c99379367676c@95.217.130.95:40656,f335bdc89890b6fa7acd75759a7aea42ea03a191@5.9.147.185:28656,324c36dcc39039d6c8007711b5923b4645c93202@142.132.202.50:46656,24be58ab07ed513a64b359174c6bb6a17fa112d4@65.109.17.86:41656,e2542af1f83025786c34947f1b6d39a511500327@173.249.20.104:26656,b3ea7a581e2f1c1e19d2067e6cd54497914ec4ea@173.249.54.237:40656,4fc14e5cccf09c1fe38ff1c896b2cda8a09c4b4d@49.12.220.38:26656,62df45d2df885de6dd2230dccf975a04005d23b3@164.68.121.197:40656,db1b1a1350e3bf1815603024dc7dcc4ef76053b6@65.109.82.106:40656,9a88a8643a1e0641f81c65f0ace6d0d44644dc37@162.55.211.136:40656,328b742040c36ed83efbd9a4b07c3bc0e3493157@62.171.158.158:26656,9dd8873f8bce7796fa6b96c1cd569ee1cff3dd36@194.163.190.91:40656,20d3366716016e41ac0d8f20954d1951565f5aab@65.109.15.207:26656,13e13cc3b1cee183592bffc1aaae6a9b3b7a7e20@38.242.206.62:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$PEERS'"|' $HOME/.defund/config/config.toml
```
