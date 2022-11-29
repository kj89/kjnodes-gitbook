# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

Website: [https://www.ollostation.zone](https://www.ollostation.zone)


## Public endpoints

* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:32656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:32659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (28)
```
peers="69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,036d17d15c4e36cee8d93f9fb1a5ad5cb956631f@213.136.76.191:26656,59fa5f6b273ea8ffb519f7bf71e329289dd2dbd7@161.97.122.177:26656,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656,9c538c7faa0881052ff1cb21c031372ab510e064@134.209.91.16:26656,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,ed38d885d068a963b0bc3986bb69680c34757a40@135.181.83.157:26656,46d6f338d845f2eabf046d8bbabdab70a7d94b18@89.179.33.100:26656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,74e60a35557efc793edb10667c3fff979ccbf49f@141.95.204.81:26656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,ad2b0a3dfdd52bb4de8624b6b378638815f8e64b@65.109.90.178:18156,4df1895f1e1d76bc317ca2698a3fea6354eadd77@65.108.15.48:26656,3baa3ab28418101d74a75e859b7ac0777f671c1c@65.108.204.119:26116,ea21f774b9a4c170a7fe4685074eef5fde7db193@116.202.236.115:22046,e8bdc07477c4a49acf1a4c91e3dc34fe2372169e@161.97.153.160:26656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,62ea32840aee3f7450089747d9b5c4a5b2110bb0@75.119.154.22:26656,43c66c6526e6fccdda693d718665941c7da4fba3@144.91.117.51:32656,4b73754c2c10d523ffd43ca95d9cb6e0ad8204a4@5.189.148.147:26656,5f2e17783db19bcf868b03a1ee0a6e2cc47df6d3@185.16.39.3:26656,958c8c3198edc57b70dd3206eb15d20e1da92bb8@185.197.195.242:36656,7b18fb68efdd736d1cd4735e38dc833f3e002f9e@89.117.49.12:32656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
