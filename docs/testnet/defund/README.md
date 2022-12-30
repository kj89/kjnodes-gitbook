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

**live-peers** (29)
```
peers="b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,c34b4bc09946950d3fb8059d4954f45ed24e25bc@89.163.255.100:26656,ad35b87df11c37b5f66931cd86c5dc2853aabae2@95.216.69.88:36656,0a1fcc2907e50b46f021389049c79f7d124f9946@77.51.200.79:36656,09ce2d3fc0fdc9d1e879888e7d72ae0fefef6e3d@65.108.105.48:11256,85518a1363fc284c2a315f0ca937ebf855783d60@65.108.238.217:11144,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,27184beff22d064a593233bbe6b0883f9f7fc2ff@45.87.104.74:26656,4eb0bef7997b87086c40766193d812479238187c@217.76.55.66:26656,d04084623a4ec44fd91d46f07ba2e2d1d0638dd4@141.95.23.183:26656,0544670a43be0a61c7e354bc55d32b6573dc31cf@94.131.106.79:26656,98a777dad655ddfbca503742107ff63fc5e0a9f5@45.147.199.212:26656,e4470dac98f2cee5bd060c52c7d801d57bfc9308@185.245.182.206:26656,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656,6854d36513081c77a24987ab66a436e29e3e5cfa@65.21.131.215:26576,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,a78c5a1fa7b12eef729fa3dec3b7c3b073552664@45.147.199.191:26656,67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656,58437bc62307a512f391db5c1e24e3cff8b9f8d3@136.243.88.91:2070,2a138efb5ef0638386af44c3df32ccdc8895b4d0@65.21.172.60:36656,35b9a1c3c7a597413f4c999a9fc1e6cb0cc8b978@65.108.100.53:36656,b914bb37cc8d1b7fb91579a79f7438a24d16de65@45.147.199.172:26656,7831e762e13c2cb99236b59f5513bf1f8d16d036@88.99.3.158:10356,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,64b6108acdddaac1097dec3045d3cf22a865c75a@65.21.196.153:26656,72ab81b6ba22876fc7f868b58efecb05ffac9753@65.109.86.236:28656,fb5f99d34d60511d947ee077ef33005e438d0c0f@185.202.223.160:26656,85279852bd306c385402185e0125dffeed36bf22@38.146.3.230:11256,b9a22be1f13a4ed99de4ecdd4c9e2a9e4711c2ac@45.147.199.190:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
