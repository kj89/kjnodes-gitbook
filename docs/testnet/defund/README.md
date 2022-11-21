# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.1.0 | **Wasm**: OFF

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

**live-peers** (23)
```
peers="26975c5bb7dc42463cc6361ea3c75f325e801917@5.161.86.214:18656,32fcb7ee30e6d31277e201e2f2d082c0aa7824e5@92.119.112.181:26656,9e1c29e75bf7dabdd43a27898148195d198a9aa0@188.34.178.184:18656,5a1977f1db820b7ee4719abbbff6f721f14176eb@65.109.84.254:36656,897e47992933105fd3c466021eaa347225edc5b2@45.147.199.48:26656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,3441bf28387afc7d9b6e7a754c3ed37f21006859@5.161.134.231:26656,bef3701487b54ba73de5e0d84ac57fc2a54f3a5f@45.147.199.67:26656,c34b4bc09946950d3fb8059d4954f45ed24e25bc@89.163.255.100:26656,fdb34ea011301410cf6231307287df27befe7049@85.114.142.242:46656,1ca28a7348da501a1d92656123692af8f9f85732@45.147.199.39:26656,13e13cc3b1cee183592bffc1aaae6a9b3b7a7e20@38.242.206.62:40656,989c2419816cc187213cd604d09b088b4d64518c@195.3.222.189:26656,57eadf177e7429db82bfdbed6fa0521e8741e404@94.130.13.40:26656,25d9dc04057628c83a3fe2406af9f1882e3ecf61@45.147.199.62:26656,695eb6029f2749c4661b716b9b9e110e0bdc5356@62.171.147.78:26656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,b3a1fda2347ffc225121793b91edd132abdcc2d9@45.147.199.63:26656,e2542af1f83025786c34947f1b6d39a511500327@173.249.20.104:26656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,62df45d2df885de6dd2230dccf975a04005d23b3@164.68.121.197:40656,90dc33a14889c0a0348b18a03d2a3d0eab41e6cb@92.119.112.225:26656,2b8e2f05af0b716b551e2d0280090cbe86316a75@124.223.26.171:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
