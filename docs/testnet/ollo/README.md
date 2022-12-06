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

**live-peers** (32)
```
peers="d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656,4b73754c2c10d523ffd43ca95d9cb6e0ad8204a4@5.189.148.147:26656,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,ed38d885d068a963b0bc3986bb69680c34757a40@135.181.83.157:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,b1c40c092d4c889d14ac8db36621c114f811d797@65.109.92.241:22046,4df1895f1e1d76bc317ca2698a3fea6354eadd77@65.108.15.48:26656,5f2e17783db19bcf868b03a1ee0a6e2cc47df6d3@185.16.39.3:26656,62ea32840aee3f7450089747d9b5c4a5b2110bb0@75.119.154.22:26656,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,3baa3ab28418101d74a75e859b7ac0777f671c1c@65.108.204.119:26116,958c8c3198edc57b70dd3206eb15d20e1da92bb8@185.197.195.242:36656,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,74e60a35557efc793edb10667c3fff979ccbf49f@141.95.204.81:26656,ad2b0a3dfdd52bb4de8624b6b378638815f8e64b@65.109.90.178:18156,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,4da239f27366a2f0076163fc577afdc67d470a82@65.109.90.33:18156,ef8863e006ba8eaea3aa8b780b01b82b401d7bd9@84.46.252.45:56656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,c5ffaa34423e83bf2d63c8780ead6977a19fa64e@65.109.30.117:36656,b1de917b6bc0e17dabd33391b2b5c5c3e99507b3@45.87.104.135:36656,46d6f338d845f2eabf046d8bbabdab70a7d94b18@89.179.33.100:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:18156"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
